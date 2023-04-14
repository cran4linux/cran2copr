%global __brp_check_rpaths %{nil}
%global packname  SDT
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Self-Determination Theory Measures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quadprog >= 1.5.5
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-quadprog >= 1.5.5
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Functions for self-determination motivation theory (SDT) to compute
measures of motivation internalization, motivation simplex structure, and
of the original and adjusted self-determination or relative autonomy
index. SDT was introduced by Deci and Ryan (1985)
<doi:10.1007/978-1-4899-2271-7>. See package?SDT for an overview.

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
