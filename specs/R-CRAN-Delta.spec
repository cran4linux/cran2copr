%global __brp_check_rpaths %{nil}
%global packname  Delta
%global packver   0.2.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Measure of Agreement Between Two Raters

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Measure of agreement delta was originally by Martín & Femia (2004)
<DOI:10.1348/000711004849268>. Since then has been considered as agreement
measure for different fields, since their behavior is usually better than
the usual kappa index by Cohen (1960) <DOI:10.1177/001316446002000104>.
The main issue with delta is that can not be computed by hand contrary to
kappa. The current algorithm is based on the Version 5 of the delta
windows program that can be found on
<https://www.ugr.es/~bioest/software/delta/cmd.php?seccion=downloads>.

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
