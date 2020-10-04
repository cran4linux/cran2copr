%global packname  detpack
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Density Estimation and Random Number Generation withDistribution Element Trees

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-parallel 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Density estimation for possibly large data sets and
conditional/unconditional random number generation or bootstrapping with
distribution element trees. The function 'det.construct' translates a
dataset into a distribution element tree. To evaluate the probability
density based on a previously computed tree at arbitrary query points, the
function 'det.query' is available. The functions 'det1' and 'det2' provide
density estimation and plotting for one- and two-dimensional datasets.
Conditional/unconditional smooth bootstrapping from an available
distribution element tree can be performed by 'det.rnd'. For more details
on distribution element trees, see: Meyer, D.W. (2016) <arXiv:1610.00345>
or Meyer, D.W., Statistics and Computing (2017)
<doi:10.1007/s11222-017-9751-9> and Meyer, D.W. (2017) <arXiv:1711.04632>
or Meyer, D.W., Journal of Computational and Graphical Statistics (2018)
<doi:10.1080/10618600.2018.1482768>.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
