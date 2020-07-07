%global packname  shapeR
%global packver   0.1-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          3%{?dist}
Summary:          Collection and Analysis of Otolith Shape Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-pixmap 
BuildRequires:    R-CRAN-wavethresh 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-MASS 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-pixmap 
Requires:         R-CRAN-wavethresh 
Requires:         R-methods 
Requires:         R-CRAN-vegan 
Requires:         R-MASS 

%description
Studies otolith shape variation among fish populations. Otoliths are
calcified structures found in the inner ear of teleost fish and their
shape has been known to vary among several fish populations and stocks,
making them very useful in taxonomy, species identification and to study
geographic variations. The package extends previously described software
used for otolith shape analysis by allowing the user to automatically
extract closed contour outlines from a large number of images, perform
smoothing to eliminate pixel noise, choose from conducting either a
Fourier or wavelet transform to the outlines and visualize the mean shape.
The output of the package are independent Fourier or wavelet coefficients
which can be directly imported into a wide range of statistical packages
in R. The package might prove useful in studies of any two dimensional
objects.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
