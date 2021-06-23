%global __brp_check_rpaths %{nil}
%global packname  imagefluency
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}%{?buildtag}
Summary:          Image Statistics Based on Processing Fluency

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-readbitmap 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-OpenImageR 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-readbitmap 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-OpenImageR 

%description
Get image statistics based on processing fluency theory. The functions
provide scores for several basic aesthetic principles that facilitate
fluent cognitive processing of images: contrast, complexity / simplicity,
self-similarity, symmetry, and typicality. See Mayer & Landwehr (2018)
<doi:10.1037/aca0000187> and Mayer & Landwehr (2018)
<doi:10.31219/osf.io/gtbhw> for the theoretical background of the methods.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/example_images
%doc %{rlibdir}/%{packname}/imageFluencyApp
%{rlibdir}/%{packname}/INDEX
