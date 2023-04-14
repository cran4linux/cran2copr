%global __brp_check_rpaths %{nil}
%global debug_package %{nil}
%global packname  cfa
%global packver   0.10-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.0
Release:          3%{?dist}%{?buildtag}
Summary:          Configural Frequency Analysis (CFA)

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch

%description
Analysis of configuration frequencies for simple and repeated measures,
multiple-samples CFA, hierarchical CFA, bootstrap CFA, functional CFA,
Kieser-Victor CFA, and Lindner's test using a conventional and an
accelerated algorithm.

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
