%global packname  rrscale
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Robust Re-Scaling to Better Recover Latent Effects in Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DEoptim 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-DEoptim 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-abind 

%description
Non-linear transformations of data to better discover latent effects.
Applies a sequence of three transformations (1) a Gaussianizing
transformation, (2) a Z-score transformation, and (3) an outlier removal
transformation. A publication describing the method has the following
citation: Gregory J. Hunt, Mark A. Dane, James E. Korkola, Laura M. Heiser
& Johann A. Gagnon-Bartsch (2020) "Automatic Transformation and
Integration to Improve Visualization and Discovery of Latent Effects in
Imaging Data", Journal of Computational and Graphical Statistics,
<doi:10.1080/10618600.2020.1741379>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
