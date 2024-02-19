%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metaplot
%global packver   0.8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.4
Release:          1%{?dist}%{?buildtag}
Summary:          Data-Driven Plot Design

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 0.7.1
BuildRequires:    R-CRAN-encode >= 0.3.6
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gtable 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-dplyr >= 0.7.1
Requires:         R-CRAN-encode >= 0.3.6
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-rlang 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gtable 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-scales 

%description
Designs plots in terms of core structure.  See 'example(metaplot)'.
Primary arguments are (unquoted) column names; order and type (numeric or
not) dictate the resulting plot.  Specify any y variables, x variable, any
groups variable, and any conditioning variables to metaplot() to generate
density plots, boxplots, mosaic plots, scatterplots, scatterplot matrices,
or conditioned plots. Use multiplot() to arrange plots in grids. Wherever
present, scalar column attributes 'label' and 'guide' are honored,
producing fully annotated plots with minimal effort. Attribute 'guide' is
typically units, but may be encoded() to provide interpretations of
categorical values (see '?encode').  Utility unpack() transforms scalar
column attributes to row values and pack() does the reverse, supporting
tool-neutral storage of metadata along with primary data. The package
supports customizable aesthetics such as such as reference lines, unity
lines, smooths, log transformation, and linear fits. The user may choose
between trellis and ggplot output. Compact syntax and integrated metadata
promote workflow scalability.

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
