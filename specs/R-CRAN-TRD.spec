%global __brp_check_rpaths %{nil}
%global packname  TRD
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Transmission Ratio Distortion

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Rlab >= 2.15.1
Requires:         R-CRAN-Rlab >= 2.15.1

%description
Transmission Ratio Distortion (TRD) is a genetic phenomenon where the two
alleles from either parent are not transmitted to the offspring at the
expected 1:1 ratio under Mendelian inheritance, leading to spurious
signals in genetic association studies. Functions in this package are
developed to account for this phenomenon using loglinear model and
Transmission Disequilibrium Test (TDT). Some population information can
also be calculated.

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
