%global packname  mixchar
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Mixture Model for the Deconvolution of Thermal Decay Curves

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-tmvtnorm 
Requires:         R-graphics 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-nloptr 
Requires:         R-stats 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-tmvtnorm 

%description
Deconvolution of thermal decay curves allows you to quantify proportions
of biomass components in plant litter. Thermal decay curves derived from
thermogravimetric analysis (TGA) are imported, modified, and then modelled
in a three- or four- part mixture model using the Fraser-Suzuki function.
The output is estimates for weights of pseudo-components corresponding to
hemicellulose, cellulose, and lignin. For more information see:
Müller-Hagedorn, M. and Bockhorn, H. (2007)
<doi:10.1016/j.jaap.2006.12.008>, Órfão, J. J. M. and Figueiredo, J. L.
(2001) <doi:10.1016/S0040-6031(01)00634-7>, and Yang, H. and Yan, R. and
Chen, H. and Zheng, C. and Lee, D. H. and Liang, D. T. (2006)
<doi:10.1021/ef0580117>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
