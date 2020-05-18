%global packname  GDAtools
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          A Toolbox for Geometric Data Analysis and More

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-moreparty 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-nleqslv 
Requires:         R-nnet 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-moreparty 

%description
Contains functions for 'specific' Multiple Correspondence Analysis, Class
Specific Analysis, Multiple Factor Analysis, 'standardized' MCA, computing
and plotting structuring factors and concentration ellipses, inductive
tests and others tools for Geometric Data Analysis (Le Roux & Rouanet
(2005) <doi:10.1007/1-4020-2236-0>). It also provides functions for the
translation of logit models coefficients into percentages (Deauvieau
(2010) <doi:10.1177/0759106309352586>), weighted contingency tables, an
association measure for contingency tables ("Percentages of Maximum
Deviation from Independence", aka PEM, see Cibois (1993)
<doi:10.1177/075910639304000103>) and some tools to measure bivariate
associations between variables (phi, Cram<c3><a9>r V, correlation
coefficient, eta-squared...).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
