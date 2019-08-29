%global packname  GDAtools
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          A Toolbox for the Analysis of Categorical Data in SocialSciences, and Especially Geometric Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-nnet 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-nleqslv 
Requires:         R-nnet 

%description
Contains functions for 'specific' MCA (Multiple Correspondence Analysis),
'class specific' MCA, computing and plotting structuring factors and
concentration ellipses, Multiple Factor Analysis, 'standardized' MCA,
inductive tests and others tools for Geometric Data Analysis. It also
provides functions for the translation of logit models coefficients into
percentages, weighted contingency tables and an association measure - i.e.
Percentages of Maximum Deviation from Independence (PEM).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
