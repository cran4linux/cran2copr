%global __brp_check_rpaths %{nil}
%global packname  durmod
%global packver   1.1-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Mixed Proportional Hazard Competing Risk Model

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.1
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp >= 1.0.1
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-nloptr 
Requires:         R-parallel 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-mvtnorm 

%description
Estimation of piecewise constant mixed proportional hazard competing risk
model with NPMLE. The model is described in S. Gaure et al. (2007)
<doi:10.1016/j.jeconom.2007.01.015>, J. Heckman and B. Singer (1984)
<doi:10.2307/1911491>, and B.G. Lindsay (1983)
<doi:10.1214/aos/1176346059>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
