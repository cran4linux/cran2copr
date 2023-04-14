%global __brp_check_rpaths %{nil}
%global packname  histogram
%global packver   0.0-25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.25
Release:          3%{?dist}%{?buildtag}
Summary:          Construction of Regular and Irregular Histograms with DifferentOptions for Automatic Choice of Bins

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Automatic construction of regular and irregular histograms as described in
Rozenholc/Mildenberger/Gather (2010).

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
