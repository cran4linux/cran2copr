%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flippant
%global packver   1.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.7
Release:          1%{?dist}%{?buildtag}
Summary:          Dithionite Scramblase Assay Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma >= 2.3.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-withr >= 2.1.2
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringi >= 1.2.3
BuildRequires:    R-CRAN-minpack.lm >= 1.2.1
BuildRequires:    R-CRAN-data.table >= 1.11.4
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-pracma >= 2.3.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-withr >= 2.1.2
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringi >= 1.2.3
Requires:         R-CRAN-minpack.lm >= 1.2.1
Requires:         R-CRAN-data.table >= 1.11.4
Requires:         R-methods 
Requires:         R-utils 

%description
The lipid scrambling activity of protein extracts and purified scramblases
is often determined using a fluorescence-based assay involving many manual
steps. flippant offers an integrated solution for the analysis and
publication-grade graphical presentation of dithionite scramblase assays,
as well as a platform for review, dissemination and extension of the
strategies it employs. The package's name derives from a play on the fact
that lipid scrambling is also sometimes referred to as 'flipping'. The
package is originally published as Cotton, R.J., Ploier, B., Goren, M.A.,
Menon, A.K., and Graumann, J. (2017). "flippant–An R package for the
automated analysis of fluorescence-based scramblase assays." BMC
Bioinformatics 18, 146. <DOI:10.1186/s12859-017-1542-y>.

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
