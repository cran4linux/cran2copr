%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TraMineR
%global packver   2.2-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Trajectory Miner: a Toolbox for Exploring and Rendering Sequences

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-vegan 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-vegan 

%description
Toolbox for the manipulation, description and rendering of categorical
sequences, and more generally the mining of sequence data in the field of
social sciences. Although this sequence analysis toolbox is primarily
intended for analyzing state or event sequences that describe life courses
such as family formation histories or professional careers, its features
also apply to many other kinds of categorical sequence data. It accepts
many different sequence representations as input and provides tools for
converting sequences from one format to another. It offers several
functions for describing and rendering sequences, for computing distances
between sequences with different metrics (among which optimal matching),
original dissimilarity-based analysis tools, and functions for extracting
the most frequent subsequences and identifying the most discriminating
ones among them. A user's guide can be found on the TraMineR web page.

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
