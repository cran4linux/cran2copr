%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nichevol
%global packver   0.1.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.20
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Ecological Niche Evolution Assessment Considering Uncertainty

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape >= 5.3
BuildRequires:    R-graphics >= 3.6
BuildRequires:    R-grDevices >= 3.6
BuildRequires:    R-stats >= 3.6
BuildRequires:    R-utils >= 3.6
BuildRequires:    R-CRAN-geiger >= 2.0
BuildRequires:    R-CRAN-terra >= 1.6
BuildRequires:    R-CRAN-castor >= 1.4
BuildRequires:    R-CRAN-stringr >= 1.4
Requires:         R-CRAN-ape >= 5.3
Requires:         R-graphics >= 3.6
Requires:         R-grDevices >= 3.6
Requires:         R-stats >= 3.6
Requires:         R-utils >= 3.6
Requires:         R-CRAN-geiger >= 2.0
Requires:         R-CRAN-terra >= 1.6
Requires:         R-CRAN-castor >= 1.4
Requires:         R-CRAN-stringr >= 1.4

%description
A collection of tools that allow users to perform critical steps in the
process of assessing ecological niche evolution over phylogenies, with
uncertainty incorporated explicitly in reconstructions. The method
proposed here for ancestral reconstruction of ecological niches
characterizes species' niches using a bin-based approach that incorporates
uncertainty in estimations. Compared to other existing methods, the
approaches presented here reduce risk of overestimation of amounts and
rates of ecological niche evolution. The main analyses include: initial
exploration of environmental data in occurrence records and accessible
areas, preparation of data for phylogenetic analyses, executing
comparative phylogenetic analyses of ecological niches, and plotting for
interpretations. Details on the theoretical background and methods used
can be found in: Owens et al. (2020) <doi:10.1002/ece3.6359>, Peterson et
al. (1999) <doi:10.1126/science.285.5431.1265>, Soberón and Peterson
(2005) <doi:10.17161/bi.v2i0.4>, Peterson (2011)
<doi:10.1111/j.1365-2699.2010.02456.x>, Barve et al. (2011)
<doi:10.1111/ecog.02671>, Machado-Stredel et al. (2021)
<doi:10.21425/F5FBG48814>, Owens et al. (2013)
<doi:10.1016/j.ecolmodel.2013.04.011>, Saupe et al. (2018)
<doi:10.1093/sysbio/syx084>, and Cobos et al. (2021)
<doi:10.1111/jav.02868>.

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
