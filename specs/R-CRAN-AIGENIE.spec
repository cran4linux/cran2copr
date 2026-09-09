%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AIGENIE
%global packver   2.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Item Generation and Validation via Network-Integrated Evaluation

License:          AGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-EGAnet >= 2.4.0
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-EGAnet >= 2.4.0
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-jsonlite 

%description
Automated psychological scale development and structural validation using
large language models (LLMs) and network psychometric methods. Implements
the AI-GENIE framework (Automatic Item Generation and Validation via
Network-Integrated Evaluation) to generate candidate items, compute
embedding representations, and estimate dimensional structure using
Exploratory Graph Analysis (EGA). Item quality is evaluated using Unique
Variable Analysis to identify redundant items and Bootstrap EGA to assess
item and dimension stability. Supports both fully automated item
generation and analysis of user-provided item sets, facilitating
efficient, theory-informed measurement development prior to empirical data
collection.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
