%global __brp_check_rpaths %{nil}
%global packname  logib
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Salary Analysis by the Swiss Federal Office for Gender Equality

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-readxl >= 1.3.1
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-readxl >= 1.3.1

%description
Implementation of the Swiss Confederation's standard analysis model for
salary analyses
<https://www.ebg.admin.ch/dam/ebg/en/dokumente/lohngleichheit/infos-zu-analysen/standard-analysemodellzurueberpruefungderlohngleichheitzwischenf.pdf.download.pdf/methodological_approachformonitoringcompliancewithwageequalitybe.pdf>
in R. The analysis is run at company-level and the model is intended for
companies with 50 or more employees (apprentices, trainees/interns and
expats are not included in the analysis). Employees with at least 100
employees are required by the Gender Equality Act to conduct an equal pay
analysis. This package allows users to run the equal salary analysis in R,
providing additional transparency with respect to the methodology and
simple automation possibilities.

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
