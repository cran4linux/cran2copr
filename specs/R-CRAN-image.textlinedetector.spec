%global __brp_check_rpaths %{nil}
%global packname  image.textlinedetector
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Segment Images in Text Lines and Words

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    opencv-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.9
BuildRequires:    R-CRAN-magick 
Requires:         R-CRAN-Rcpp >= 0.12.9
Requires:         R-CRAN-magick 

%description
Find text lines in scanned images and segment the lines into words.
Includes implementations of the paper 'Novel A* Path Planning Algorithm
for Line Segmentation of Handwritten Documents' by Surinta O. et al (2014)
<doi:10.1109/ICFHR.2014.37> available at
<https://github.com/smeucci/LineSegm>, an implementation of 'A Statistical
approach to line segmentation in handwritten documents' by Arivazhagan M.
et al (2007) <doi:10.1117/12.704538>, and a wrapper for an image
segmentation technique to detect words in text lines as described in the
paper 'Scale Space Technique for Word Segmentation in Handwritten
Documents' by Manmatha R. and Srimal N. (1999) paper at
<doi:10.1007/3-540-48236-9_3>, wrapper for code available at
<https://github.com/arthurflor23/text-segmentation>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
