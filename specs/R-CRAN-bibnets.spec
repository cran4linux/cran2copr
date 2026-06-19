%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bibnets
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}%{?buildtag}
Summary:          Importing, Constructing, and Exporting Bibliometric Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-utils 

%description
Imports, constructs, and exports bibliometric networks from scholarly
metadata. Reads 'Scopus', 'Web of Science', 'BibTeX', 'RIS', 'OpenAlex',
'Lens.org', 'Dimensions', and 'Crossref' exports. Goes beyond standard
co-networks with attention-weighted networks (lead, last, proximity,
circular position weights), position-aware counting (harmonic, arithmetic,
geometric, golden-ratio), similarity and dissimilarity normalisations,
temporal networks with fixed, sliding, and cumulative windows,
disparity-filter backbone extraction, historiograph construction, and
local citation scoring. Methods described in López-Pernas, Saqr & Apiola
(2023) <doi:10.1007/978-3-031-25336-2_5>.

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
