%global packname  mFLICA
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}
Summary:          Leadership-Inference Framework for Multivariate Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0
BuildRequires:    R-CRAN-dtw 
Requires:         R-CRAN-ggplot2 >= 3.0
Requires:         R-CRAN-dtw 

%description
A leadership-inference framework for multivariate time series. The
framework for multiple-faction-leadership inference from coordinated
activities or 'mFLICA' uses a notion of a leader as an individual who
initiates collective patterns that everyone in a group follows. Given a
set of time series of individual activities, our goal is to identify
periods of coordinated activity, find factions of coordination if more
than one exist, as well as identify leaders of each faction. For each time
step, the framework infers following relations between individual time
series, then identifying a leader of each faction whom many individuals
follow but it follows no one. A faction is defined as a group of
individuals that everyone follows the same leader. 'mFLICA' reports
following relations, leaders of factions, and members of each faction for
each time step. Please see Chainarong Amornbunchornvej and Tanya
Berger-Wolf (2018) <doi:10.1137/1.9781611975321.62> when referring to this
package in publications.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
