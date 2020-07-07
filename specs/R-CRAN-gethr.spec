%global packname  gethr
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Access to Ethereum-Based Blockchains Through Geth Nodes

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-httr 

%description
Full access to the Geth command line interface for running full Ethereum
nodes. With gethr it is possible to carry out different tasks such as mine
ether, transfer funds, create contacts, explore block history, etc. The
package also provides access to all the available APIs. The officially
exposed by Ethereum blockchains (eth, shh, web3, net) and some provided
directly by Geth (admin, debug, miner, personal, txpool). For more details
on Ethereum, access the project website <https://www.ethereum.org/>. For
more details on the Geth client, access the project website
<https://github.com/ethereum/go-ethereum/wiki/geth/>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
