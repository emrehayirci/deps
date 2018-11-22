import { Box, Text } from "grommet";
import React, { Component } from 'react';
import { connect } from 'react-redux';
import './home.css';


const mapStateToProps = state => {
    return {
        notes: state.posts,
    }
}

const mapDispatchToProps = dispatch => {
    return {}
}

class Home extends Component {
  render() {
    return (
      <Box>
        <Text size={'xxlarge'}> Wow this is Deps! And It is using Grommet </Text>
      </Box>
    );
  }
}



export default  connect(mapStateToProps, mapDispatchToProps)(Home);
