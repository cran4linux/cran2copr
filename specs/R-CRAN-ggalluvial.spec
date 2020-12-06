%global packname  ggalluvial
%global packver   0.12.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12.3
Release:          1%{?dist}%{?buildtag}
Summary:          Alluvial Plots in 'ggplot2'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2
BuildRequires:    R-CRAN-dplyr >= 0.7
BuildRequires:    R-CRAN-tidyr >= 0.7
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-ggplot2 >= 2.2
Requires:         R-CRAN-dplyr >= 0.7
Requires:         R-CRAN-tidyr >= 0.7
Requires:         R-stats 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 

%description
Alluvial plots use variable-width ribbons and stacked bar plots to
represent multi-dimensional or repeated-measures data with categorical or
ordinal variables; see Riehmann, Hanfler, and Froehlich (2005)
<doi:10.1109/INFVIS.2005.1532152> and Rosvall and Bergstrom (2010)
<doi:10.1371/journal.pone.0008694>. Alluvial plots are statistical
graphics in the sense of Wilkinson (2006) <doi:10.1007/0-387-28695-0>;
they share elements with Sankey diagrams and parallel sets plots but are
uniquely determined from the data and a small set of parameters. This
package extends Wickham's (2010) <doi:10.1198/jcgs.2009.07098> layered
grammar of graphics to generate alluvial plots from tidy data.

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
