%global __brp_check_rpaths %{nil}
%global packname  SOAR
%global packver   0.99-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.11
Release:          3%{?dist}%{?buildtag}
Summary:          Memory management in R by delayed assignments

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildArch:        noarch

%description
Allows objects to be stored on disc and automatically recalled into
memory, as required, by delayed assignment.

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
