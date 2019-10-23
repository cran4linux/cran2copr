%global packname  photobiologyPlants
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}
Summary:          Plant Photobiology Related Functions and Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-photobiology >= 0.9.28
BuildRequires:    R-CRAN-photobiologyWavebands >= 0.4.3
Requires:         R-CRAN-photobiology >= 0.9.28
Requires:         R-CRAN-photobiologyWavebands >= 0.4.3

%description
Provides functions for quantifying visible (VIS) and ultraviolet (UV)
radiation in relation to the photoreceptors Phytochromes, Cryptochromes,
and UVR8 which are present in plants. It also includes data sets on the
optical properties of plants. Part of the 'r4photobiology' suite, Aphalo
P. J. (2015) <doi:10.19232/uv4pb.2015.1.14>.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
