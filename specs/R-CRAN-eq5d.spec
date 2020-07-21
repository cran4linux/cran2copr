%global packname  eq5d
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}
Summary:          Methods for Calculating 'EQ-5D' Utility Index Scores

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
EQ-5D is a popular health related quality of life instrument used in the
clinical and economic evaluation of health care. Developed by the EuroQol
group <https://www.euroqol.org>, the instrument consists of two
components: health state description and evaluation. For the description
component a subject self-rates their health in terms of five dimensions;
mobility, self-care, usual activities, pain/discomfort, and
anxiety/depression using either a three-level (EQ-5D-3L,
<https://www.euroqol.org/eq-5d-instruments/eq-5d-3l-about>) or a
five-level (EQ-5D-5L,
<https://www.euroqol.org/eq-5d-instruments/eq-5d-5l-about>) scale.
Frequently the scores on these five dimensions are converted to a single
utility index using country specific value sets, which can be used in the
clinical and economic evaluation of health care as well as in population
health surveys. The eq5d package provides methods to calculate index
scores from a subject's dimension scores. 25 TTO and 11 VAS EQ-5D-3L value
sets including those for countries in Szende et al (2007)
<doi:10.1007/1-4020-5511-0> and Szende et al (2014)
<doi:10.1007/978-94-007-7596-1>, 22 EQ-5D-5L EQ-VT value sets from the
EuroQol website, and the EQ-5D-5L crosswalk value sets developed by van
Hout et al. (2012) <doi:10.1016/j.jval.2012.02.008> are included.
Additionally, a shiny web tool is included to enable the calculation,
visualisation and automated statistical analysis of EQ-5D index values via
a web browser using EQ-5D dimension scores stored in CSV or Excel files.

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
