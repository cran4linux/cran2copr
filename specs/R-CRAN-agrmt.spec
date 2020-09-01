%global packname  agrmt
%global packver   1.42.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.42.4
Release:          1%{?dist}%{?buildtag}
Summary:          Calculate Concentration and Dispersion in Ordered Rating Scales

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Calculates concentration and dispersion in ordered rating scales. It
implements various measures of concentration and dispersion to describe
what researchers variably call agreement, concentration, consensus,
dispersion, or polarization among respondents in ordered data. It also
implements other related measures to classify distributions. In addition
to a generic city-block based concentration measure and a generic
dispersion measure, the package implements various measures, including van
der Eijk's (2001) <DOI: 10.1023/A:1010374114305> measure of agreement A,
measures of concentration by Leik, Tatsle and Wierman, Blair and Lacy,
Kvalseth, Berry and Mielke, Reardon, and Garcia-Montalvo and
Reynal-Querol. Furthermore, the package provides an implementation of
Galtungs AJUS-system to classify distributions, as well as a function to
identify the position of multiple modes.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
