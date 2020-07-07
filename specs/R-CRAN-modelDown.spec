%global packname  modelDown
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Make Static HTML Website for Predictive Models

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-archivist >= 2.1.0
BuildRequires:    R-CRAN-devtools >= 2.0.1
BuildRequires:    R-CRAN-psych >= 1.8.4
BuildRequires:    R-CRAN-svglite >= 1.2.1
BuildRequires:    R-CRAN-DALEX >= 1.0
BuildRequires:    R-CRAN-kableExtra >= 0.9.0
BuildRequires:    R-CRAN-DT >= 0.4
BuildRequires:    R-CRAN-whisker >= 0.3
BuildRequires:    R-CRAN-auditor >= 0.3.0
BuildRequires:    R-CRAN-drifter >= 0.2.1
BuildRequires:    R-CRAN-breakDown >= 0.1.6
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-archivist >= 2.1.0
Requires:         R-CRAN-devtools >= 2.0.1
Requires:         R-CRAN-psych >= 1.8.4
Requires:         R-CRAN-svglite >= 1.2.1
Requires:         R-CRAN-DALEX >= 1.0
Requires:         R-CRAN-kableExtra >= 0.9.0
Requires:         R-CRAN-DT >= 0.4
Requires:         R-CRAN-whisker >= 0.3
Requires:         R-CRAN-auditor >= 0.3.0
Requires:         R-CRAN-drifter >= 0.2.1
Requires:         R-CRAN-breakDown >= 0.1.6

%description
Website generator with HTML summaries for predictive models. This package
uses 'DALEX' explainers to describe global model behavior. We can see how
well models behave (tabs: Model Performance, Auditor), how much each
variable contributes to predictions (tabs: Variable Response) and which
variables are the most important for a given model (tabs: Variable
Importance). We can also compare Concept Drift for pairs of models (tabs:
Drifter). Additionally, data available on the website can be easily
recreated in current R session. Work on this package was financially
supported by the NCN Opus grant 2017/27/B/ST6/01307 at Warsaw University
of Technology, Faculty of Mathematics and Information Science.

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

%files
%{rlibdir}/%{packname}
