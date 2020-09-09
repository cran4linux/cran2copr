%global packname  rock
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Reproducible Open Coding Kit

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-utils >= 3.5.0
BuildRequires:    R-graphics >= 3.0.0
BuildRequires:    R-stats >= 3.0.0
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-DiagrammeR >= 1.0.0
BuildRequires:    R-CRAN-data.tree >= 0.7.8
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-CRAN-yum >= 0.0.1
Requires:         R-utils >= 3.5.0
Requires:         R-graphics >= 3.0.0
Requires:         R-stats >= 3.0.0
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-DiagrammeR >= 1.0.0
Requires:         R-CRAN-data.tree >= 0.7.8
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-CRAN-yum >= 0.0.1

%description
The Reproducible Open Coding Kit ('ROCK', and this package, 'rock') was
developed to facilitate reproducible and open coding, specifically geared
towards qualitative research methods. Although it is a general-purpose
toolkit, three specific applications have been implemented, specifically
an interface to the 'rENA' package that implements Epistemic Network
Analysis ('ENA'), means to process notes from Cognitive Interviews
('CIs'), and means to work with decentralized construct taxonomies
('DCTs').

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
