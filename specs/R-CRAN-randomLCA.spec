%global packname  randomLCA
%global packver   1.0-16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.16
Release:          2%{?dist}
Summary:          Random Effects Latent Class Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-lattice 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-parallel 
Requires:         R-lattice 
Requires:         R-boot 
Requires:         R-CRAN-fastGHQuad 
Requires:         R-Matrix 
Requires:         R-CRAN-Rfast 
Requires:         R-parallel 

%description
Fits standard and random effects latent class models. The single level
random effects model is described in Qu et al <doi:10.2307/2533043> and
the two level random effects model in Beath and Heller
<doi:10.1177/1471082X0800900302>. Examples are given for their use in
diagnostic testing.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
