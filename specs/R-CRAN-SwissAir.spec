%global __brp_check_rpaths %{nil}
%global packname  SwissAir
%global packver   1.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.5
Release:          3%{?dist}%{?buildtag}
Summary:          Air Quality Data of Switzerland for One Year in 30 MinResolution

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.1
Requires:         R-core >= 2.13.1
BuildArch:        noarch

%description
Ozone, NOx (= Sum of nitrogen monoxide and nitrogen dioxide), nitrogen
monoxide, ambient temperature, dew point, wind speed and wind direction at
3 sites around lake of Lucerne in Central Switzerland in 30 min time
resolution for year 2004.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/INDEX
