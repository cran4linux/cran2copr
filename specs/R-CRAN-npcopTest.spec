%global __brp_check_rpaths %{nil}
%global packname  npcopTest
%global packver   1.03
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.03
Release:          3%{?dist}%{?buildtag}
Summary:          Non Parametric Test for Detecting Changes in the Copula

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
A non parametric test for change points detection in the dependence
between the components of multivariate data, with or without (multiple)
changes in the marginal distributions. The full details, justification and
examples are published in Rohmer (2016) <doi:10.1016/j.spl.2016.06.026>.

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
