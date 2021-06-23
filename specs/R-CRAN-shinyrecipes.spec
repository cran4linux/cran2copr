%global __brp_check_rpaths %{nil}
%global packname  shinyrecipes
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Gadget to Use the Data Preprocessing 'recipes' PackageInteractively

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-shinyWidgets 
BuildRequires:    R-CRAN-shinyglide 
BuildRequires:    R-CRAN-sortable 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-esquisse 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-shinyWidgets 
Requires:         R-CRAN-shinyglide 
Requires:         R-CRAN-sortable 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-esquisse 

%description
This gadget allows you to use the 'recipes' package belonging to
'tidymodels' to carry out the data preprocessing tasks in an interactive
way. Build your 'recipe' by dragging the variables, visually analyze your
data to decide which steps to use, add those steps and preprocess your
data.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/script
%{rlibdir}/%{packname}/INDEX
