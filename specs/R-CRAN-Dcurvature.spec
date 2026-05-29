%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Dcurvature
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete Curvature with 'shiny' Explorer

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-readxl 

%description
Implements discrete curvature estimation for ordered planar point
sequences using circumcenter geometry on consecutive triplets, exposed
through compiled C plus plus (C++) code via 'Rcpp' for speed and numerical
robustness. The package is useful for objective elbow detection in
multivariate workflows, especially principal component analysis (PCA),
where selecting the number of retained components can be subjective. It
provides a 'shiny' interface that supports upload of raw datasets or
explained-variance tables, computes Kaiser-Meyer-Olkin (KMO)
sampling-adequacy diagnostics, evaluates individual and cumulative
variance curves, and reports curvature- based decision rules (m* and m**)
with visual summaries for reproducible component-selection decisions.
References: Arney et al. (2001); Axler (2024)
<doi:10.1007/978-3-031-41026-0>; Bjorklund (2019) <doi:10.1111/evo.13835>;
Burden and Faires (2015); Chang et al. (2023)
<https://CRAN.R-project.org/package=shiny>; Christensen (2019); Cui (2020)
<doi:10.18637/jss.v040.i08>; Eddelbuettel and Sanderson (2014)
<doi:10.1016/j.csda.2013.02.005>; Engelke et al. (2023)
<doi:10.1016/j.jseint.2023.04.010>; Gniazdowski (2021)
<doi:10.26348/znwwsi.24.35>; Haynes et al. (2017); Jameel and Al-Salami
(2023) <doi:10.24086/cuejhss.v7n1y2023.pp121-125>; Jolliffe (2002);
Jolliffe and Cadima (2016) <doi:10.1098/rsta.2015.0202>; Kaiser (1974);
Lehnert et al. (2019) <doi:10.18637/jss.v089.i12>; Ma and Dai (2011)
<doi:10.1093/bib/bbq090>; Milligan (1995); Onumanyi et al. (2022)
<doi:10.3390/app12157515>; Park (2010); Revelle (2024)
<https://CRAN.R-project.org/package=psych>; Rodionova et al. (2021)
<doi:10.1016/j.chemolab.2021.104304>; Sen and Cohen (2025)
<doi:10.1177/01466216251344288>; Serneels and Verdonck (2008)
<doi:10.1016/j.csda.2007.05.024>; Shi et al. (2021)
<doi:10.1186/s13638-021-01910-w>; Shaukat et al. (2016)
<doi:10.1515/eko-2016-0014>; Syakur et al. (2018)
<doi:10.1088/1757-899X/336/1/012017>; Wickham and Bryan (2023)
<https://CRAN.R-project.org/package=readxl>; Wu et al. (2017)
<doi:10.1088/1755-1315/61/1/012054>; Youssef et al. (2023)
<doi:10.21303/2461-4262.2023.002582>.

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
