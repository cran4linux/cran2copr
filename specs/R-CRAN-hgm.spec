%global __brp_check_rpaths %{nil}
%global packname  hgm
%global packver   1.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.18
Release:          3%{?dist}%{?buildtag}
Summary:          Holonomic Gradient Method and Gradient Descent

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildRequires:    R-CRAN-deSolve 
Requires:         R-CRAN-deSolve 

%description
The holonomic gradient method (HGM, hgm) gives a way to evaluate
normalization constants of unnormalized probability distributions by
utilizing holonomic systems of differential or difference equations. The
holonomic gradient descent (HGD, hgd) gives a method to find maximal
likelihood estimates by utilizing the HGM.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
