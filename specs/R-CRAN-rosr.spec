%global packname  rosr
%global packver   0.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.10
Release:          1%{?dist}
Summary:          Create Reproducible Research Projects

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc >= 2.0
BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-bookdown 
BuildRequires:    R-CRAN-blogdown 
BuildRequires:    R-CRAN-tinytex 
BuildRequires:    R-CRAN-mindr 
BuildRequires:    R-CRAN-bookdownplus 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-clipr 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-bookdown 
Requires:         R-CRAN-blogdown 
Requires:         R-CRAN-tinytex 
Requires:         R-CRAN-mindr 
Requires:         R-CRAN-bookdownplus 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-clipr 
Requires:         R-CRAN-knitr 

%description
Creates reproducible academic projects with integrated academic elements,
including datasets, references, codes, images, manuscripts, dissertations,
slides and so on. These elements are well connected so that they can be
easily synchronized and updated.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/rmarkdown
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/skeleton
%{rlibdir}/%{packname}/INDEX
