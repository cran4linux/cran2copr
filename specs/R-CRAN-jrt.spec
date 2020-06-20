%global packname  jrt
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Item Response Theory Modeling and Scoring for Judgment Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-directlabels >= 2017.03.31
BuildRequires:    R-CRAN-ggsci >= 2.9
BuildRequires:    R-CRAN-psych >= 1.8.3.3
BuildRequires:    R-CRAN-mirt >= 1.30
BuildRequires:    R-CRAN-irr >= 0.84
BuildRequires:    R-CRAN-tidyr >= 0.8.3
BuildRequires:    R-CRAN-dplyr >= 0.7.7
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-directlabels >= 2017.03.31
Requires:         R-CRAN-ggsci >= 2.9
Requires:         R-CRAN-psych >= 1.8.3.3
Requires:         R-CRAN-mirt >= 1.30
Requires:         R-CRAN-irr >= 0.84
Requires:         R-CRAN-tidyr >= 0.8.3
Requires:         R-CRAN-dplyr >= 0.7.7
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 

%description
Psychometric analysis and scoring of judgment data using polytomous
Item-Response Theory (IRT) models, as described in Myszkowski and Storme
(2019) <doi:10.1037/aca0000225>. A convenience function is used to
automatically compare and select models, as well as to present a variety
of model-based statistics. Plotting functions are used to present category
curves, as well as information, reliability and standard error functions.

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
