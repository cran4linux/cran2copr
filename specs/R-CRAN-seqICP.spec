%global __brp_check_rpaths %{nil}
%global packname  seqICP
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Sequential Invariant Causal Prediction

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-dHSIC 
BuildRequires:    R-mgcv 
BuildRequires:    R-stats 
Requires:         R-CRAN-dHSIC 
Requires:         R-mgcv 
Requires:         R-stats 

%description
Contains an implementation of invariant causal prediction for sequential
data. The main function in the package is 'seqICP', which performs linear
sequential invariant causal prediction and has guaranteed type I error
control. For non-linear dependencies the package also contains a
non-linear method 'seqICPnl', which allows to input any regression
procedure and performs tests based on a permutation approach that is only
approximately correct. In order to test whether an individual set S is
invariant the package contains the subroutines 'seqICP.s' and 'seqICPnl.s'
corresponding to the respective main methods.

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
