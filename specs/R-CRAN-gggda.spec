%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gggda
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          A 'ggplot2' Extension for Geometric Data Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-labeling 
BuildRequires:    R-CRAN-ddalpha 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-labeling 
Requires:         R-CRAN-ddalpha 

%description
A variety of multivariable data summary statistics and constructions have
been proposed, either to generalize univariable analogs or to exploit
multivariable properties. Notable among these are the bivariate peelings
surveyed by Green (1981, ISBN:978-0-471-28039-2), the bag-and-bolster
plots proposed by Rousseeuw &al (1999)
<doi:10.1080/00031305.1999.10474494>, and the minimum spanning trees used
by Jolliffe (2002) <doi:10.1007/b98835> to represent high-dimensional
relationships among data in a low-dimensional plot. Additionally, biplots
of singular value--decomposed tabular data, such as from principal
components analysis, make use of vectors, calibrated axes, and other
representations of variable elements to complement point markers for case
elements; see Gabriel (1971) <doi:10.1093/biomet/58.3.453> and Gower &
Harding (1988) <doi:10.1093/biomet/75.3.445> for original proposals.
Because they treat the abscissa and ordinate as commensurate or the data
elements themselves as point masses or unit vectors, these multivariable
tools can be thought of as belonging to geometric data analysis; see
Podani (2000, ISBN:90-5782-067-6) for techniques and applications and Le
Roux & Rouanet (2005) <doi:10.1007/1-4020-2236-0> for foundations. 'gggda'
extends Wickham's (2010) <doi:10.1198/jcgs.2009.07098> layered grammar of
graphics with statistical transformation ("stat") and geometric
construction ("geom") layers for many of these tools, as well as
convenience coordinate systems to emphasize intrinsic geometry of the
data.

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
