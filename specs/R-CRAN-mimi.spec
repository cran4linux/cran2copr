%global __brp_check_rpaths %{nil}
%global packname  mimi
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Main Effects and Interactions in Mixed and Incomplete Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-softImpute 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-rARPACK 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-softImpute 
Requires:         R-stats 
Requires:         R-CRAN-FactoMineR 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-rARPACK 

%description
Generalized low-rank models for mixed and incomplete data frames. The main
function may be used for dimensionality reduction of imputation of
numeric, binary and count data (simultaneously). Main effects such as
column means, group effects, or effects of row-column side information
(e.g. user/item attributes in recommendation system) may also be modelled
in addition to the low-rank model. Geneviève Robin, Olga Klopp, Julie
Josse, Éric Moulines, Robert Tibshirani (2018) <arXiv:1806.09734>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
