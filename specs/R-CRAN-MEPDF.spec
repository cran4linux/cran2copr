%global packname  MEPDF
%global packver   3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0
Release:          3%{?dist}%{?buildtag}
Summary:          Creation of Empirical Density Functions Based on MultivariateData

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-gtools 

%description
Based on the input data an n-dimensional cube with sub cells of user
specified side length is created. The number of sample points which fall
in each sub cube is counted, and with the cell volume and overall sample
size an empirical probability can be computed. A number of cubes of higher
resolution can be superimposed. The basic method stems from J.L. Bentley
in "Multidimensional Divide and Conquer". J. L. Bentley (1980)
<doi:10.1145/358841.358850>. Furthermore a simple kernel density
estimation method is made available, as well as an expansion of Bentleys
method, which offers a kernel approach for the grid method.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
