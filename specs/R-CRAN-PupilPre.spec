%global packname  PupilPre
%global packver   0.6.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.2
Release:          3%{?dist}
Summary:          Preprocessing Pupil Size Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats >= 3.3.2
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-zoo >= 1.8.4
BuildRequires:    R-mgcv >= 1.8.16
BuildRequires:    R-CRAN-VWPre >= 1.2.0
BuildRequires:    R-CRAN-robustbase >= 0.93.3
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-signal >= 0.7.6
BuildRequires:    R-CRAN-tidyr >= 0.6.0
BuildRequires:    R-CRAN-shiny >= 0.14.2
BuildRequires:    R-CRAN-rlang >= 0.1.1
Requires:         R-stats >= 3.3.2
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-zoo >= 1.8.4
Requires:         R-mgcv >= 1.8.16
Requires:         R-CRAN-VWPre >= 1.2.0
Requires:         R-CRAN-robustbase >= 0.93.3
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-signal >= 0.7.6
Requires:         R-CRAN-tidyr >= 0.6.0
Requires:         R-CRAN-shiny >= 0.14.2
Requires:         R-CRAN-rlang >= 0.1.1

%description
Pupillometric data collected using SR Research Eyelink eye trackers
requires significant preprocessing. This package contains functions for
preparing pupil dilation data for visualization and statistical analysis.
Specifically, it provides a pipeline of functions which aid in data
validation, the removal of blinks/artifacts, downsampling, and baselining,
among others. Additionally, plotting functions for creating grand average
and conditional average plots are provided. See the vignette for samples
of the functionality. The package is designed for handling data collected
with SR Research Eyelink eye trackers using Sample Reports created in SR
Research Data Viewer.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
