%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eiballots
%global packver   0.1.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Ballot-Level Microdata and Summaries for Ecological Inference (Florida 2000)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Provides access to ballot-level electoral microdata from the Florida 2000
general election and tools for computing summaries suitable for ecological
inference. Includes functions to load data by county or race (election),
compute marginal distributions at the precinct level, and build joint
contingency arrays across multiple races for use with ecological inference
packages. Data files are stored in a remote repository and downloaded on
demand; local copies are supported via the 'data_dir' option.
Acknowledgements: We thank Jaime Ventura (ANES, University of Michigan)
and Dan Keating (The Washington Post) for providing the raw data that
serve as the starting point for the construction of this package. We also
acknowledge funding from the Conselleria de Educación, Cultura y
Universidades (grant CIACIO/2023/031).

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
