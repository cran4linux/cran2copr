%global __brp_check_rpaths %{nil}
%global packname  fugue
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          3%{?dist}%{?buildtag}
Summary:          Sensitivity Analysis Optimized for Matched Sets of Varied Sizes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
As in music, a fugue statistic repeats a theme in small variations.  Here,
the psi-function that defines an m-statistic is slightly altered to
maintain the same design sensitivity in matched sets of different sizes.
The main functions in the package are sen() and senCI().  For sensitivity
analyses for m-statistics, see Rosenbaum (2007) Biometrics 63 456-464
<doi:10.1111/j.1541-0420.2006.00717.x>.

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
