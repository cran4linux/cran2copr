%global packname  BIRDS
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Biodiversity Information Review and Decision Support

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.0
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-geosphere >= 1.5
BuildRequires:    R-CRAN-rgdal >= 1.5
BuildRequires:    R-CRAN-sp >= 1.4.4
BuildRequires:    R-CRAN-stringr >= 1.4
BuildRequires:    R-CRAN-shiny >= 1.0
BuildRequires:    R-CRAN-sf >= 0.7
BuildRequires:    R-CRAN-mapedit >= 0.5
BuildRequires:    R-CRAN-rgeos >= 0.4
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-esquisse 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-shotGroups 
BuildRequires:    R-CRAN-taxize 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-xts 
Requires:         R-CRAN-leaflet >= 2.0
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-geosphere >= 1.5
Requires:         R-CRAN-rgdal >= 1.5
Requires:         R-CRAN-sp >= 1.4.4
Requires:         R-CRAN-stringr >= 1.4
Requires:         R-CRAN-shiny >= 1.0
Requires:         R-CRAN-sf >= 0.7
Requires:         R-CRAN-mapedit >= 0.5
Requires:         R-CRAN-rgeos >= 0.4
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-esquisse 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-shotGroups 
Requires:         R-CRAN-taxize 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-xts 

%description
It helps making the evaluation and preparation of biodiversity data easy,
systematic and reproducible. It also helps the users to overlay the point
observations into a custom grid that is useful for further analysis. The
review summarise statistics that helps evaluate whether a set of species
observations is fit-for-use and take decisions upon its use of on further
analyses. It does so by quantifying the sampling effort (amount of effort
expended during an event) and data completeness (data gaps) to help judge
whether the data is representative, valid and fit for any intended
purpose. The 'BIRDS' package is most useful when working with
heterogeneous data sets with variation in the sampling process, i.e. where
data have been collected and reported in various ways and therefore
varying in sampling effort and data completeness (i.e. how well the
reported observations describe the true state). Primary biodiversity data
(PBD) combining data from different data sets, like e.g. Global
Biodiversity Information Facility (GBIF) mediated data, commonly vary in
the ways data has been generated - containing opportunistically collected
presence-only data together with and data from systematic monitoring
programs. The set of tools provided is aimed at understanding the process
that generated the data (i.e. observing, recording and reporting species
into databases). There is a non-vital function on this package
(makeDggrid()) that depends the package 'dggridR' that is no longer on
CRAN. You can find it here <https://github.com/r-barnes/dggridR>.
References: Ruete (2015) <doi:10.3897/BDJ.3.e5361>; Szabo, Vesk, Baxter &
Possingham (2010) <doi:10.1890/09-0877.1>; Telfer, Preston 6 Rothery
(2002) <doi:10.1016/S0006-3207(02)00050-2>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
