%global __brp_check_rpaths %{nil}
%global packname  GFGM.copula
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Generalized Farlie-Gumbel-Morgenstern Copula

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-cmprsk 
BuildRequires:    R-CRAN-compound.Cox 
BuildRequires:    R-CRAN-joint.Cox 
Requires:         R-CRAN-cmprsk 
Requires:         R-CRAN-compound.Cox 
Requires:         R-CRAN-joint.Cox 

%description
Compute bivariate dependence measures and perform bivariate competing
risks analysis under the generalized Farlie-Gumbel-Morgenstern (FGM)
copula. See Shih and Emura (2018) <doi:10.1007/s00180-018-0804-0> and Shih
and Emura (2019) <doi:10.1007/s00362-016-0865-5> for details.

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
