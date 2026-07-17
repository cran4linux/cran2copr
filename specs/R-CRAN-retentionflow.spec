%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  retentionflow
%global packver   0.1.25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.25
Release:          1%{?dist}%{?buildtag}
Summary:          Retention Flow Tables and Sankey Diagrams

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch

%description
Creates transition tables, summaries, and interactive Sankey diagrams from
longitudinal person-term-state data. Sankey diagrams visualize flows
between states with link widths proportional to flow counts; see Kennedy
and Sankey (1898) "The Thermal Efficiency of Steam Engines"
<doi:10.1680/imotp.1898.19100> and Schmidt (2008) "The Sankey Diagram in
Energy and Material Flow Management: Part I: History"
<doi:10.1111/j.1530-9290.2008.00004.x>. The minimum input schema is one
row per person per term with an identifier, term, and categorical state.

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
