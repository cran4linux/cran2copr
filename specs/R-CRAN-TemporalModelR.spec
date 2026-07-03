%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TemporalModelR
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Temporally Explicit Species Distribution Modelling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-exactextractr 
Requires:         R-CRAN-deldir 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-exactextractr 

%description
Increases the ease of implementing a temporally-explicit modeling
methodology when building ecological niche and species distribution
models. Provides functions to assist with three major steps of
temporally-explicit models: (i) preprocessing species and environmental
data and generating suitable background or pseudoabsence data, (ii)
building a niche model and generating temporally-explicit predictions from
that model, and (iii) model postprocessing to explore spatiotemporal
trends in model predictions. Methodological and theoretical foundations
are described in Ingenloff and Peterson (2021)
<doi:10.1111/2041-210X.13564>, Franklin (2010, ISBN:9780521700023),
Peterson et al. (2011, ISBN:9780691136882), Blonder (2018)
<doi:10.1111/ecog.03187>, Senay et al. (2013)
<doi:10.1371/journal.pone.0071218>, and Li and Zhang (2024)
<doi:10.48550/arXiv.2404.05933>.

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
