%global __brp_check_rpaths %{nil}
%global packname  daterangepicker
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Create a Shiny Date-Range Input

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonify 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonify 
Requires:         R-CRAN-shiny 

%description
A Shiny Input for date-ranges, which pops up two calendars for selecting
dates, times, or predefined ranges like "Last 30 Days". It wraps the
JavaScript library 'daterangepicker' which is available at
<https://www.daterangepicker.com>.

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
%{rlibdir}/%{packname}
