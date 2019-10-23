%global packname  rlme
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          Rank-Based Estimation and Prediction in Random Effects NestedModels

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-nlme 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
Requires:         R-MASS 
Requires:         R-CRAN-quantreg 
Requires:         R-nlme 
Requires:         R-mgcv 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 

%description
Estimates robust rank-based fixed effects and predicts robust random
effects in two- and three- level random effects nested models. The
methodology is described in Bilgic & Susmann (2013)
<https://journal.r-project.org/archive/2013/RJ-2013-027/>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
