%global __brp_check_rpaths %{nil}
%global packname  forwards
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Data from Surveys Conducted by Forwards

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Anonymized data from surveys conducted by Forwards
<https://forwards.github.io/>, the R Foundation task force on women and
other under-represented groups. Currently, a single data set of responses
to a survey of attendees at useR! 2016
<https://www.r-project.org/useR-2016/>, the R user conference held at
Stanford University, Stanford, California, USA, June 27 - June 30 2016.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
