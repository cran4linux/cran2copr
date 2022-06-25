%global __brp_check_rpaths %{nil}
%global packname  HDStIM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          High Dimensional Stimulation Immune Mapping ('HDStIM')

License:          CC0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-Boruta 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-Boruta 
Requires:         R-CRAN-scales 

%description
A method for identifying responses to experimental stimulation in mass or
flow cytometry that uses high dimensional analysis of measured parameters
and can be performed with an end-to-end unsupervised approach. In the
context of in vitro stimulation assays where high-parameter cytometry was
used to monitor intracellular response markers, using cell populations
annotated either through automated clustering or manual gating for a
combined set of stimulated and unstimulated samples, 'HDStIM' labels cells
as responding or non-responding. The package also provides auxiliary
functions to rank intracellular markers based on their contribution to
identifying responses and generating diagnostic plots.

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
